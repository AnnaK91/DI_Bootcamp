import random
import string

def get_random_password(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random password of length", length, "is:", result_str)

get_random_password(256)



class Config:
    SECRET_KEY = "sirgtjewwgdehxptmchhfxuvfehwfdbanassnyexdycxcdydezwmuoylxgpahvnindljdqesedhohgwhkqbcysfcucphnjurgribelzozuvmnomfqinjhjntqmdpcbenomudxdasslhdxojskezxlykojdiuicrohbriqlfbmcxijzoczftssyhvciytpqvbxfmspdarvtmqulipyyxmxshylxhfipphcioxlpkaebgpesibnyupyxvibfmcdcpk"
