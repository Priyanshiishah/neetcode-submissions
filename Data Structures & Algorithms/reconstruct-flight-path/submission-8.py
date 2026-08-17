class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}

        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        # Track which outgoing edge is already used
        used = {
            src: [False] * len(adj[src])
            for src in adj
        }

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in adj:
                return False

            for i, v in enumerate(adj[src]):
                if used[src][i]:
                    continue

                # Choose
                used[src][i] = True
                res.append(v)

                # Explore
                if dfs(v):
                    return True

                # Backtrack
                res.pop()
                used[src][i] = False

            return False

        dfs("JFK")
        return res