class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0

        while target != 1:
            if target % 2 != 0:
                # the target is odd
                steps += 1
                print(f"odd {target}")
                target -= 1
            
            # Now all targets are even

            if maxDoubles > 0:
                print(f"even {target}")
                target = int(target / 2)
                maxDoubles -= 1
                steps += 1
            else:
                break
        print(f"steps {steps}, target {target-1}")
        steps += target - 1
        return steps