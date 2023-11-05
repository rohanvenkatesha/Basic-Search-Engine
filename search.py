import string

# Clean the tokens by removing punctuation and checking if the char is alpha and return the clean token or empty if it is not alpha.
def cleanToken(token):
    cleaned_token = token.strip(string.punctuation) #Remove Punctuations
    is_alpha = False
    for char in cleaned_token:
        if char.isalpha(): #check if alpha
            is_alpha = True
            break
    if is_alpha and len(cleaned_token)>1:
        return cleaned_token.lower() #convert to lowercase
    else:
        return ""
    
# Create the inverted index by reversing the key value pairs received from the forward index, where the key is a collection of tokenized words and the values are URLs.
def buildInvertedIndex(docs):
    inverted_index = {}
    for url, tokens in docs.items():  #fetch key-values from foward index dictionary
        for token in tokens:
            if token not in inverted_index:
                inverted_index[token] = set()
            inverted_index[token].add(url)  #swap key-values and build invereted index
    return inverted_index

# Search the inverted index keys for the entered query, and then show the values of the corresponding index keys' URLs.
def findQueryMatches(index, query):
    querysplit = query.split()
    output_url = set()
    for value in querysplit:
        operator = ""
        if value.startswith('+'):  #Check if operator startswith '+'
            operator = '+'
            value = value[1:]
        elif value.startswith('-'):  #Check if operator startswith '-'
            operator = '-'
            value = value[1:]
        clean_value = cleanToken(value)
        if clean_value and clean_value in index:
            result = index[clean_value]
            if operator == '+':
                output_url.intersection_update(result)   #perform intersection of sets
            elif operator == '-':
                output_url.difference_update(result)   #perform difference of sets
            else:
                output_url.update(result)    #perform updation of sets
    return output_url

# Create the forward index after reading the data file and return dictionary with a key-value pair, where the key is the URL and the value is a set of tokenized words.
def readDocs(dbfile):
    readdocs = {}
    url = None
    content = ""
    cleaned_tokens = set()
    pagebodyflag=False

    # Read the Sample data file and perform tokenization.
    with open(dbfile, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()   #Remove spaces from begining and end of lines
            if line.startswith("<pageBody>"):
                pagebodyflag=True
            elif line.startswith("<endPageBody>"):
                pagebodyflag=False
                url=None
            elif line.startswith("http") and pagebodyflag==False:
                if not url:
                    url = line     #Fetching the url
                    content = ""
            else:
                if url:
                    content = content+ " " + line 
                    tokens = content.split()
                    cleaned_tokens = set(cleanToken(token) for token in tokens)
                    readdocs[url] = cleaned_tokens      #Mapping the url to set of cleaned_tokens values
    return readdocs  #return dictionary

# Create a search engine that accepts query input and displays URL results.
def mySearchEngine(dbfile):
    readdocs = readDocs(dbfile)   #forwardindex
    inverted_index = buildInvertedIndex(readdocs)  #invereted index
    len_url = len(readdocs)
    token_lengths = []
    for tokens in readdocs.values():
        token_lengths.append(len(tokens))
    print("Stand while building index...")
    print("Indexed", len_url, "pages containing ",sum(token_lengths)," unique terms.")
    while True:
        query = input("Enter a search query (or empty string to quit): ")   #fetch the query from user
        if not query:
            break
        matches = findQueryMatches(inverted_index, query)    #call findQueryMatches method to search the required query
        print("Found ",len(matches)," Matching Pages ")
        if matches:
            print(matches)   #Print the matches

if __name__ == "__main__":
    mySearchEngine("/workspaces/Basic-Search-Engine/sampleWebsiteData.txt")   #sample dbfile