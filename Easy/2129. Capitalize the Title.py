class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([word.lower() if len(word) <= 2 else word.title() for word in title.split(" ") ])
        #ANOTHER METHOD
        '''newTitle = []
        title = title.split()
        for word in title:
            if len(word) <= 2:
                word = word.lower()
            else:
                word = word.capitalize()
            newTitle.append(word)      
        return ' '.join(newTitle)'''         