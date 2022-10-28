morse_alpha_dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "	..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
}

morse_num_dict = {
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

morse_sym_dict = {
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.",
    ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.", "¿": "..-.-", "¡": "--...-"
}


def get_encode(msg: str) -> str:
    encoded_word = ""
    for letter in msg:
        if letter in morse_alpha_dict:
            encoded_word += f"{morse_alpha_dict[letter]} "
        elif letter in morse_num_dict:
            encoded_word += f"{morse_num_dict[letter]} "
        elif letter in morse_sym_dict:
            encoded_word += f"{morse_sym_dict[letter]} "
        elif letter == " ":
            encoded_word += "* "
    return encoded_word


def get_decode(msg: list) -> str:
    inv_alpha_dict = {value: key for key, value in morse_alpha_dict.items()}
    inv_num_dict = {value: key for key, value in morse_num_dict.items()}
    inv_sym_dict = {value: key for key, value in morse_sym_dict.items()}

    decoded_word = ""
    for morse in msg:
        if morse in inv_alpha_dict:
            decoded_word += inv_alpha_dict[morse]
        elif morse in inv_num_dict:
            decoded_word += inv_num_dict[morse]
        elif morse in inv_sym_dict:
            decoded_word += inv_sym_dict[morse]
        elif morse == "*":
            decoded_word += " "
        else:
            decoded_word += ""
    return decoded_word


def morse_converter():
    convert_type = input('Which action would you like to choose? Type "encode", "decode", or "stop": ').lower()

    if convert_type == "encode":
        encode_msg = input("Please type the message you would like to encode: ").lower()

        morse_code = get_encode(str(encode_msg))
        print(morse_code)
        morse_converter()
    elif convert_type == "decode":
        decode_msg = input(
            "Please type the morse code separated by spaces and words separated by ' * ' (e.g.: .- -... * -.-):\n")

        word = get_decode(decode_msg.split(" "))
        print(word)
        morse_converter()
    elif convert_type == "stop":
        print("Thank you for using the morse code converter!")
    else:
        morse_converter()


print("Welcome to the morse code converter!")
morse_converter()
