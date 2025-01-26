class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans=[]
        for i in range(len(favoriteCompanies)):
            isSubset=False
            for j in range(len(favoriteCompanies)):
                if i!=j:
                    x=set(favoriteCompanies[i])
                    y=set(favoriteCompanies[j])
                    if len(x.difference(y))==0:
                        isSubset=True
                        break
            if isSubset==False:
                ans.append(i)
        return ans

#

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans=[]
        dictionary = {i:set(arr) for i,arr in enumerate(favoriteCompanies)}

        for i in range(len(favoriteCompanies)):
            isSubset=False
            for j in range(len(favoriteCompanies)):
                if i!=j:
                    if dictionary[i].issubset(dictionary[j]):
                        isSubset=True
                        break
            if isSubset==False:
                ans.append(i)
        return ans