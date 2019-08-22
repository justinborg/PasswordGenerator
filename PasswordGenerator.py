import string
import random

def generate_password(**kwargs):
    generated_password = ""
    population = []
    if kwargs["uppercase"] in ["Y","y"]:
        population += string.ascii_uppercase
    if kwargs["lowercase"] in ["Y","y"]:
        population += string.ascii_lowercase
    if kwargs["punctuation"] in ["Y","y"]:
        population += string.punctuation
    if kwargs["digits"] in ["Y","y"]:
        population += string.digits
    for i in range(kwargs["length"]):
        generated_password += random.choice(population)
    return generated_password

def main():
    length = -1
    uppercase = "D"
    lowercase = "D"
    punctuation = "D"
    digits = "D"
    while length < 0:
        length = input("Input Password Length (>0): ")
        length = int(length)
    while uppercase not in ["Y","N","y","n"]:
        uppercase = input("Do you want uppercase letters? (Y,N): ")
    while lowercase not in ["Y", "N", "y", "n"]:
        lowercase = input("Do you want lowercase letters? (Y,N): ")
    while punctuation not in ["Y", "N", "y", "n"]:
        punctuation = input("Do you want punctuations? (Y,N): ")
    while digits not in ["Y", "N", "y", "n"]:
        digits = input("Do you want digits? (Y,N): ")
    mydict = {
        "length":length,
        "uppercase":uppercase,
        "lowercase":lowercase,
        "punctuation":punctuation,
        "digits":digits
    }
    print(generate_password(**mydict))

if __name__ == "__main__":
    main()