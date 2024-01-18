# Challenge Title

Array-Reverse

## Whiteboard Process

<![Whiteboard Solution](<whiteboard.jpg>)

## Approach & Efficiency

I saw some YouTube videos recently about sorting, so I decided to use left and right technique to work outside-in. I reassigned the left index position to right side and vice-versa.

## Resources

- ChatGPT was used to remind me how to use the left/right technique.

## Solution

```def array_reverse(arr):
    if len(arr) <= 1:
        return arr

    else:
        start_position = 0
        end_position = len(arr) - 1

        while start_position < end_position:
            arr[start_position] = arr[end_position]
            arr[end_position] = arr[start_position]
            start_position += 1
            end_position -= 1

        return arr```
