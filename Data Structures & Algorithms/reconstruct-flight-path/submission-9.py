from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}

        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        # Track which ticket from each source has been used
        used = {
            src: [False] * len(adj[src])
            for src in adj
        }

        res = ["JFK"]

        def dfs(src):
            # If we used all tickets, itinerary is complete
            if len(res) == len(tickets) + 1:
                return True

            # Dead end before using all tickets
            if src not in adj:
                return False

            # Try destinations in lexical order
            for i, dst in enumerate(adj[src]):
                if used[src][i]:
                    continue

                # Choose
                used[src][i] = True
                res.append(dst)

                # Explore
                if dfs(dst):
                    return True

                # Backtrack
                res.pop()
                used[src][i] = False

            return False

        dfs("JFK")

        return res