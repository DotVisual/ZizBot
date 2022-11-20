import phonenumbers, shlex, sys
from phonenumbers import carrier, geocoder, timezone
zizcodingde = " ".join(map(shlex.quote, sys.argv[1:]))
zizcodingde = f"+{zizcodingde}"
#mobileNo=input("Mobile no. with country code:")
print (f"Info Nomor: {zizcodingde}")
mobileNo=zizcodingde
mobileNo=phonenumbers.parse(mobileNo)
print(timezone.time_zones_for_number(mobileNo))
print('```provider / sim```: '+carrier.name_for_number(mobileNo,"en"))
print('```Negara```: '+geocoder.description_for_number(mobileNo,"en"))
print("```Nomor Yang Valid?```:",phonenumbers.is_valid_number(mobileNo))
print("```possibility```:",phonenumbers.is_possible_number(mobileNo))
print ("_Script By ZizCodingDE_")
