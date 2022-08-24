def celciusAFarenheit(grados):
    gradosF = 1.8*grados+32
    return gradosF

def celciusAKelvin(grados):
    gradosK = grados + 273.15
    return gradosK

print("Farenheit: ",celciusAFarenheit(30))
print("Kelvin: ",celciusAKelvin(30))
input()