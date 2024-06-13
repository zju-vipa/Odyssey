# Tutorials/Morse code
Morse code is a method of transmitting information in a series of dots and dashes. A dot is a short redstone pulse, a dash is a long pulse. Dashes are approximately three times as long as dots. In Minecraft, there aren't any specific uses for creating a communication device, but it can be an interesting experiment.

## Contents
- 1 Introduction
	- 1.1 The Sender
	- 1.2 The Decoder
	- 1.3 The Translator

## Introduction
For Morse code to be able to be sent and received in Minecraft, redstone circuits will be required. There are two main gates for first decoding the signal: an AND gate and RS-NOR latch. It's recommended that you read up on those and get familiar with them before proceeding. There are three main sections of this: the Sender, which will create the signal required; a Decoder, which turns the signal into a series of lights indicating the dots and the dashes; and finally a Translator, which can be connected to turn that information into a single light representing the letter sent.

### The Sender

This is the simplest of the three sections; all that needs to be achieved from this is something that can later be decoded into either a dot or a dash. To do this, you will need to make the signal for a dash longer than that of the signal for a dot. This can be achieved by using what has become known as 'Monostable Circuits'; which are easy to produce due to redstone repeaters. As repeaters can also be set on a delay, you can use this to increase the time take for the message to be sent through the wire. 
Monostable Circuit/Pulse Lengthener (long)
. This will be used for the dash and the reset option, which will be created later. The dot doesn't require any delay or extension as it can be detected by the fact that it hasn't been increased.

### The Decoder
Now, after the 'Sender', this is going to be much more complicated. What you want to be able to do here is a system to be able to understand the dots and the dashes and convert that into a light display. To explain this, it's best if just explain from the image.

Monostable Circuit/Pulse Lengthener (long)
Here you can see one section of the decoding system. The initial decoder doesn't require the first AND gate and instead comes straight from the input 'I'. When the first input comes through it will be sent into a length detecting and gate 'B' or the repeater and gate, if the signal is long enough it will be able to pass through this and gate and then power the rs-nor 'C', which will then allow the Q for dash to be on. If the length of the signal is not long enough to pass through 'B' it will then not activate the Rs-nor, instead it will just go where the signal also goes which is round to the next 'C^', rs-nor which once switched will send a signal round to 'B' therefore not allowing any more signals to pass through. When this happens the power from the 3rd input of the 3 input 'and' gate 'B' will go to the Q(dot). If the power for the dash is on then it will over ride the dot turning it off, if it's on otherwise if the dash had been activated and then the signal goes through the dot would also be on, so you will need to make the dot turn off when dash is on, you can do this as shown, feeding the power back into the Q dot.

You will notice that at 'B' there is four repeaters delaying the message to the 3rd input this is because you need to allow time, if it’s there, for the dash to pass through and then block the gate so it can no longer be affected by any other impulse. The rs-nor 'C^' which activates the 3rd input also goes into another and gate which when the next impulse comes through will allow the signal to pass and go the same process again as before.

That about does it for the decoder.

To build the reseter, you need to just place redstone torches under all the rs-nors and then have a repeater 'and' gate the requires more than a dash would and set up a button for that, it is would recommended to use a delay after the gate as well to make sure that no other things will change when you send the reset through the system. Also remember that you want the lights to be OFF, default and then turn on when you want to reset.

