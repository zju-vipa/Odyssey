"""
Tests for MiniMax LLM provider in Multi-Agent Odyssey framework.
"""
import json
import unittest
from unittest.mock import MagicMock, patch, mock_open
from langchain.schema import AIMessage, HumanMessage, SystemMessage


# ---------------------------------------------------------------------------
# Helpers for patching the module-level config load in llm.py
# ---------------------------------------------------------------------------

MOCK_CONFIG = {
    "openai_key": "sk-openai-test",
    "dashscope_key": "sk-ali-test",
    "deepseek_key": "sk-deepseek-test",
    "minimax_key": "sk-minimax-test",
    "server_host": "localhost",
    "server_port": "8000",
    "NODE_SERVER_PORT": 3000,
    "MC_SERVER_HOST": "localhost",
    "MC_SERVER_PORT": "25565",
}


def _mock_open_config(*args, **kwargs):
    return mock_open(read_data=json.dumps(MOCK_CONFIG))()


# ---------------------------------------------------------------------------
# Unit tests
# ---------------------------------------------------------------------------

class TestModelType(unittest.TestCase):
    """Verify ModelType constants are defined correctly."""

    def setUp(self):
        # Patch the file open so the import succeeds without a real config.json
        patcher = patch("builtins.open", side_effect=_mock_open_config)
        patcher.start()
        self.addCleanup(patcher.stop)

        import importlib
        import odyssey.agents.llm as llm_module
        importlib.reload(llm_module)
        self.llm = llm_module

    def test_minimax_constant(self):
        self.assertEqual(self.llm.ModelType.MINIMAX, "minimax")

    def test_all_expected_types_present(self):
        mt = self.llm.ModelType
        for attr in ("LLAMA2_70B", "LLAMA3_8B", "LLAMA3_70B", "DEEPSEEK", "GPT", "ALI", "MINIMAX"):
            self.assertTrue(hasattr(mt, attr), f"ModelType missing: {attr}")


class TestCallWithMessagesMiniMax(unittest.TestCase):
    """Unit tests for the MiniMax branch in call_with_messages."""

    def _get_module(self):
        with patch("builtins.open", side_effect=_mock_open_config):
            import importlib
            import odyssey.agents.llm as llm_module
            importlib.reload(llm_module)
            return llm_module

    def _make_messages(self, system="You are a Minecraft agent.", user="What should I do next?"):
        return [SystemMessage(content=system), HumanMessage(content=user)]

    def _mock_openai_response(self, text="Build a shelter."):
        mock_choice = MagicMock()
        mock_choice.message.content = text
        mock_response = MagicMock()
        mock_response.choices = [mock_choice]
        return mock_response

    @patch("builtins.open", side_effect=_mock_open_config)
    def test_minimax_returns_ai_message(self, _):
        llm = self._get_module()
        msgs = self._make_messages()

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = self._mock_openai_response("Mine wood first.")

        with patch("odyssey.agents.llm.OpenAI", return_value=mock_client):
            result = llm.call_with_messages(msgs, model_type=llm.ModelType.MINIMAX)

        self.assertIsInstance(result, AIMessage)
        self.assertEqual(result.content, "Mine wood first.")

    @patch("builtins.open", side_effect=_mock_open_config)
    def test_minimax_uses_correct_base_url(self, _):
        llm = self._get_module()
        msgs = self._make_messages()

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = self._mock_openai_response()

        with patch("odyssey.agents.llm.OpenAI", return_value=mock_client) as mock_openai_cls:
            llm.call_with_messages(msgs, model_type=llm.ModelType.MINIMAX)

        call_kwargs = mock_openai_cls.call_args.kwargs
        self.assertEqual(call_kwargs.get("base_url"), "https://api.minimax.io/v1")
        self.assertEqual(call_kwargs.get("api_key"), "sk-minimax-test")

    @patch("builtins.open", side_effect=_mock_open_config)
    def test_minimax_default_model(self, _):
        llm = self._get_module()
        msgs = self._make_messages()

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = self._mock_openai_response()

        with patch("odyssey.agents.llm.OpenAI", return_value=mock_client):
            llm.call_with_messages(msgs, model_type=llm.ModelType.MINIMAX)

        create_kwargs = mock_client.chat.completions.create.call_args.kwargs
        self.assertEqual(create_kwargs.get("model"), "MiniMax-M2.7")

    @patch("builtins.open", side_effect=_mock_open_config)
    def test_minimax_custom_model(self, _):
        llm = self._get_module()
        msgs = self._make_messages()

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = self._mock_openai_response()

        with patch("odyssey.agents.llm.OpenAI", return_value=mock_client):
            llm.call_with_messages(
                msgs, model_type=llm.ModelType.MINIMAX, minimax_model="MiniMax-M2.7-highspeed"
            )

        create_kwargs = mock_client.chat.completions.create.call_args.kwargs
        self.assertEqual(create_kwargs.get("model"), "MiniMax-M2.7-highspeed")

    @patch("builtins.open", side_effect=_mock_open_config)
    def test_minimax_temperature_in_range(self, _):
        """Temperature must be in (0.0, 1.0] per MiniMax API requirements."""
        llm = self._get_module()
        msgs = self._make_messages()

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = self._mock_openai_response()

        with patch("odyssey.agents.llm.OpenAI", return_value=mock_client):
            llm.call_with_messages(msgs, model_type=llm.ModelType.MINIMAX)

        create_kwargs = mock_client.chat.completions.create.call_args.kwargs
        temp = create_kwargs.get("temperature")
        self.assertIsNotNone(temp)
        self.assertGreater(temp, 0.0)
        self.assertLessEqual(temp, 1.0)

    @patch("builtins.open", side_effect=_mock_open_config)
    def test_minimax_passes_system_and_user_messages(self, _):
        llm = self._get_module()
        system_text = "You are a skilled Minecraft agent."
        user_text = "How do I craft a pickaxe?"
        msgs = self._make_messages(system=system_text, user=user_text)

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = self._mock_openai_response()

        with patch("odyssey.agents.llm.OpenAI", return_value=mock_client):
            llm.call_with_messages(msgs, model_type=llm.ModelType.MINIMAX)

        create_kwargs = mock_client.chat.completions.create.call_args.kwargs
        messages_sent = create_kwargs.get("messages", [])
        self.assertEqual(messages_sent[0]["role"], "system")
        self.assertEqual(messages_sent[0]["content"], system_text)
        self.assertEqual(messages_sent[1]["role"], "user")
        self.assertEqual(messages_sent[1]["content"], user_text)

    @patch("builtins.open", side_effect=_mock_open_config)
    def test_minimax_handles_api_error_gracefully(self, _):
        llm = self._get_module()
        msgs = self._make_messages()

        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = Exception("API error")

        with patch("odyssey.agents.llm.OpenAI", return_value=mock_client):
            # Should not raise; prints error and returns None
            result = llm.call_with_messages(msgs, model_type=llm.ModelType.MINIMAX)

        self.assertIsNone(result)

    @patch("builtins.open", side_effect=_mock_open_config)
    def test_minimax_not_used_for_other_model_types(self, _):
        """Ensure MiniMax client is NOT instantiated for non-MiniMax model types."""
        llm = self._get_module()
        msgs = self._make_messages()

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = self._mock_openai_response()

        with patch("odyssey.agents.llm.OpenAI", return_value=mock_client) as mock_cls:
            llm.call_with_messages(msgs, model_type=llm.ModelType.GPT)

        # For GPT calls, base_url should not be minimax
        if mock_cls.called:
            call_kwargs = mock_cls.call_args.kwargs
            self.assertNotEqual(
                call_kwargs.get("base_url", ""), "https://api.minimax.io/v1"
            )


# ---------------------------------------------------------------------------
# Integration test (skipped unless MINIMAX_API_KEY is set)
# ---------------------------------------------------------------------------

class TestMiniMaxIntegration(unittest.TestCase):
    """Integration test — requires MINIMAX_API_KEY env variable."""

    def setUp(self):
        import os
        self.api_key = os.environ.get("MINIMAX_API_KEY")
        if not self.api_key:
            self.skipTest("MINIMAX_API_KEY not set — skipping integration test")

    def test_live_minimax_call(self):
        import os
        config_data = {
            "minimax_key": self.api_key,
            "openai_key": "",
            "dashscope_key": "",
            "deepseek_key": "",
            "server_host": "localhost",
            "server_port": "8000",
            "NODE_SERVER_PORT": 3000,
            "MC_SERVER_HOST": "localhost",
            "MC_SERVER_PORT": "25565",
        }
        with patch("builtins.open", mock_open(read_data=json.dumps(config_data))):
            import importlib
            import odyssey.agents.llm as llm_module
            importlib.reload(llm_module)

        msgs = [
            SystemMessage(content="You are a helpful Minecraft assistant."),
            HumanMessage(content="Reply with exactly: 'MiniMax ready'"),
        ]
        result = llm_module.call_with_messages(msgs, model_type=llm_module.ModelType.MINIMAX)
        self.assertIsInstance(result, AIMessage)
        self.assertGreater(len(result.content), 0)

    def test_live_minimax_highspeed_model(self):
        import os
        config_data = {
            "minimax_key": self.api_key,
            "openai_key": "",
            "dashscope_key": "",
            "deepseek_key": "",
            "server_host": "localhost",
            "server_port": "8000",
            "NODE_SERVER_PORT": 3000,
            "MC_SERVER_HOST": "localhost",
            "MC_SERVER_PORT": "25565",
        }
        with patch("builtins.open", mock_open(read_data=json.dumps(config_data))):
            import importlib
            import odyssey.agents.llm as llm_module
            importlib.reload(llm_module)

        msgs = [
            SystemMessage(content="You are a helpful Minecraft assistant."),
            HumanMessage(content="What is the first step to survive in Minecraft? Answer in one sentence."),
        ]
        result = llm_module.call_with_messages(
            msgs,
            model_type=llm_module.ModelType.MINIMAX,
            minimax_model="MiniMax-M2.7-highspeed",
        )
        self.assertIsInstance(result, AIMessage)
        self.assertGreater(len(result.content), 0)


if __name__ == "__main__":
    unittest.main()
