def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    frequencies = {}
    
    #iterate through the string object and remove punctuations and creating a new string
    new_file_contents = ""
    for char in file_contents:
        if char not in punctuations:
            new_file_contents += char
            
                
    #convert the string input object into lower case words and also make it a list by splitting the string
    list1 = new_file_contents.lower().split()
    
    #remove the uninteresting words from the list, iterating through two lists and comparing the words one by one
    for element in list1:
        for word in uninteresting_words:
            if element == word:
                list1.remove(word)
            
        
    
    
    # Here the code is putting the words and frequencies into the dictionary
    for word in list1:
        if word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1
        
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()
