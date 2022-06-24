# Boilerplate Binary Tree

Here's some boilerplate code for creating and visualizing Binary Trees. Oftentimes when I'm trying to create the visual representation of a Binary Tree I find myself spending so much time hitting Tab and adjusting the space between nodes that I forget what I needed the Tree for in the first place. To help with this problem, I wrote some boilerplate to save time and will hopefully save some time for you as well. Feel free to use and/or contribute!

## Constraints

#### At the moment...

- Works best with single character values and/or None/null values.
- Hasn't really been tested with Trees taller than 5 levels.

## How to use

- Create a single TreeNode

  ```
  node = TreeNode(10)
  print(node)             ->    <**main**.TreeNode object at 0x102684f70>
  print(node.value)       ->    10
  print(node.left)        ->    None
  print(node.right)       ->    None
  ```

- Create a Binary Tree from an array and print it as an array

  ```
  arr = [1, 2, 3, 4, 5, 6, 7, None, 9, None, 1, 2, None, 4, 5]
  tree = TreeNode.from_array(arr)
  print(tree)             ->    <**main**.TreeNode object at 0x1027fe370>
  print(tree.to_array())  ->    [1, 2, 3, 4, 5, 6, 7, None, 9, None, 1, 2, None, 4, 5]
  ```

- Create a PrintableTree from a Tree instance

  ```
  printable_tree = TreePrinter(tree)
  print(printable_tree.visualize())   ->

                 1

         2               3

     4       5       6       7

   -   9   -   1   2   -   4   5
  ```

## Contribute

Please submit pull requests to make this better!

It would be awesome to get translations for JS, Java, C++, etc!
