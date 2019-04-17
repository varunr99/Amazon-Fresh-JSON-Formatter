import json

# Open output file and add beginning entries
output = open("output.json","w") 
output.write("{\n") 
output.write("  \"ingredients\": [\n")

# Find contents of shoppingList json
name = []
amount = []
asinOverride = []
with open('shoppingList.json') as json_file:
    data = json.load(json_file)
    for i in data['shoppingList']:
        for j in data['shoppingList'].get(i):
            for k in data['shoppingList'].get(i).get(j):
                if (k == 'name'):
                    # This will print the name
                    name.append(data['shoppingList'].get(i).get(j).get(k))
                if (k == 'amount'):
                    amount.append(data['shoppingList'].get(i).get(j).get(k))
                # This accounts for added-in asin override, will be useless for now
                if (k == 'asinOverride'):
                    asinOverride.append(data['shoppingList'].get(i).get(j).get(k))


# Counter that keeps track of number of entries so we can correctly place comma
entry = 0
for i in range(len(name)):
    # Print some necessary brackets
    output.write("    {\n")
    # Print the name to the json file, deal with avocado edge case
    if (name[i] == "Avocado (mashed)"):
        output.write("      \"name\": \"Avocado\", \n")
    else:
        output.write("      \"name\": \"" + name[i] + "\",\n")
    # Print blank asin override (we'll replace this when we add those)
    output.write("      \"asinOverride\": \"\",\n")
    # Uncomment the code below when you add in asinOverrides and delete above asin code
    # output.write("      \"name\": \"" + asinOverride[i] + "\",\n")
    # Print quantity list stuff
    output.write("      \"quantityList\": [\n")
    # Iterate through list here
    # Also, reset qList counter in each case
    qList = 0
    for key, value in amount[i].items():
        output.write("       {\n")
        if (key == 'cup'):
            # Print all necessary stuff
            output.write("          \"unit\": \"CUPS\",\n")
        elif (key == 'oz'):
            # Print all necessary stuff
            output.write("          \"unit\": \"OUNCES\",\n")
        elif (key == 'whole'):
            output.write("          \"unit\": \"COUNT\",\n")
        # Add more cases
        elif (key == 'tbsp'):
            output.write("          \"unit\": \"TBSP\",\n")
        elif (key == 'tsp'):
            output.write("          \"unit\": \"TSP\",\n")
        elif (key == 'slice'):
            output.write("          \"unit\": \"SLICES\",\n")
        elif (key == 'pinch'):
            output.write("          \"unit\": \"PINCHES\",\n")
        output.write("          \"amount\": " + str(value))
        if (qList == len(amount[i].items()) - 1):
            output.write("\n        }\n")
        else:
            output.write("\n        },\n")
        qList += 1
    output.write("      ]\n")
    # Print some necessary end stuff
    if (entry == len(name) - 1):
        output.write("    }\n")
    else:
        output.write("    },\n")
    entry += 1



# Write ending brackets/braces to output file
output.write("  ]\n")
output.write("}")

output.close()