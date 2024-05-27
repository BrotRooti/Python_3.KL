
alphabet = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..",
            "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-",
            "Y":"-.--", "Z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...",
            "8":"---..", "9":"----.", ".":".-.-.-", ",":"--..--", "?":"..--..", "'":".----.", "!":"-.-.--", "/":"-..-.", "(":"-.--.", ")":"-.--.-",
            "&":".-...", ":":"---...", ";":"-.-.-.", "=":"-...-", "+":".-.-.", "-":"-....-", "_":"..--.-", '"':".-..-.", "$":"...-..-", "@":".--.-.", " ":"/"
            }

"""
Encodes a string of text to a series of slashes dots and dashes, where slash represents a stop, dot a short signal and dash a long signal
"""
def encode(text):
    text = text.upper()
    encoded = ""
    for char in text:
        if char in alphabet:
            encoded += str(alphabet[char])
            encoded += "/"
    return encoded

"""
Decodes a string of 0s 1s and 2s back to a text string, where 0 represents a stop, 1 a short signal and 2 a long signal
"""
def decode(text):
    decoded = ""
    text = text.split("/")
    for char in text:
        for key, value in alphabet.items():
            if char == str(value):
                decoded += key
    return decoded

def use (text, short_delay, long_delay, stop_signal):
    out = []
    morse_text = encode(text)
    for i in morse_text:
        for n in  i:
            if n == ".":
                out.append(short_delay)
            elif n=="-":
                out.append(long_delay)
            else:
                out.append(stop_signal)
    return out


