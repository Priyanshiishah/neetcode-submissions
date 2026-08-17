class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}

        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        used = {src: [False] * len(dsts) for src, dsts in adj.items()}
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                if used[src][i]:                                       
                    continue                                          
                used[src][i] = True                                     
                res.append(v)
                if dfs(v): 
                    return True
                used[src][i] = False
                res.pop()
            return False

        dfs("JFK")
        return res