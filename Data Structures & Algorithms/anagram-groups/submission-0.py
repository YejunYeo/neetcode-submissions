class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        arr = []

        cnt1 = 0
        cnt2 = 0
        flag = True
        while (flag == True):
            res = "".join(sorted(strs[cnt1]))
            if res not in hashmap:
                hashmap[res] = cnt2
                arr.append([strs[cnt1]])
                cnt2 += 1
            else:
                idx = hashmap.get(res)
                arr[idx].append(strs[cnt1])

            cnt1 +=1
            if cnt1 == len(strs):
                break
        return arr
        