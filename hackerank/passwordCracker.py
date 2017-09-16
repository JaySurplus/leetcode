"""
    Password Cracker
    https://www.hackerrank.com/challenges/password-cracker/problem
"""
import sys

sys.setrecursionlimit(2000)


class Solution():
    def solver(self, passwords, target):
        target_set = set(target)
        word_set = set(passwords)
        l_set = set("".join(passwords))


        if target_set > l_set:
            res = "WRONG PASSWORD"
        elif target_set <= word_set:
            res = " ".join(list(target))
        else:
            ans = ""
            mem = set()
            dic = {}
            for w in word_set:
                if w[0] not in dic:
                    dic[w[0]] = [w]
                else:
                    dic[w[0]].append(w)
            res = self.helper(dic, target, ans, mem)
            res = "WRONG PASSWORD" if res == "" else res
        return res

    def helper(self, dic, target, ans, mem ):

        if target == "":
            return ans
        if target in mem:
            return ""

        if target[0] in dic:
            for w in dic[target[0]]:
                if w == target[:len(w)]:
                    curr_ans = self.helper(dic, target[len(w):], ans + w + " ", mem)
                    if curr_ans != "":
                        return curr_ans
        mem.add(target)
        return ""

if __name__ == '__main__':
    sol = Solution()
    passwords = ['the', 'cake', 'is', 'a', 'lie', 'thec', 'ak', 'ei', 'sal', 'ie']
    target = "thecakeisalithecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieeithecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieaiethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieeitheisthecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalie"


    passwords = ['solo', 'love', 'vest', 'stop', 'open', 'ends', 'dsso']
    target = "opendssovestdssolostloveendsopenstopdssodssoloveopenstopendssolodssoopensolosoloopenendssololovelovestopstopveststopendsendssolovestendsstopvestloveendsvestendssoloendsveststopopenlovedssosolovestopendssolovestoplovedssolovedssolovelostvestvestlostsolovestdssodssoendslovestopstopendssololovestopopenvestloveloveendsvestendsdssovestlovesolovestopensolosoloopendssovestopendssovestendsdssosoloendsdssostopstopstopvestopensolosolovestsolostoplovestoplovestopvestlovelovelovelovestopdssodssodssosolovestdssovestvestlovestopstopendsvestopenopenvestlovevestdssoopenendssoloendsopenopenendsstopdssoendssoloendsdssostopvestvestloveendsvestlostlovesoloendsloveloveloveopenloveendsdssoopenvestvestopensololoveloveendsdssoendsvestlovelovelovevestloveloveveststopsolodssoendsstopstopdssolovelovedssoendsdssoendssoloendsendsstopdssovestendsopendssoendslovedssovestdssosolovestsolosolodssosolostopopenlovedssoendsloveendsendsstopstoplovelostopenendssololovevestsololovestopstoplovestopopensolodssostopendsstopsolosoloendsdssosoloopenlostopensoloendsdssoendsdssostopopenstopstopstopendslovestopvestdssosolostopveststopvestsolostopstopsolovestveststoploveloveendssoloopenlostlovedssosololovestopstopvestsololostsololoveopenvestloveopenveststopsoloveststoploveendssoloopensoloopenvestsoloopenvestveststopdssosolovestvestvestdssoendsvestdssoopenopendssodssostoplovevestlovesololovelovesolosolodssosololovedssosolosoloendssolovestvestopenstopopenopenlovesoloveststopsolovestsoloendsvestopenstopsololovevestsolosololovestopopensolovestvestdssostoploveopendssostopdssodssoendsdssolovesolosolosolosololovelostvestsolodssoopendssodssodssovestvestopendssoopenstopdssolovestopsolostopstopdssolovedssosolovestopensolostopdssostopopenendssoloendsvestvestveststopendsopenendsstopvestdssosolosoloopenendssolosolodssosolovestsololoveendsvestendslovelovestopsoloendsendsdssostopvestdssosolostopsolodssosoloendsloveendsveststopopenvestdssostoploveendslostdssoopendssovestsoloendsendslostlostopenendsstopdssovestendsvestdssosolovest"
    print(sol.solver(passwords, target))
