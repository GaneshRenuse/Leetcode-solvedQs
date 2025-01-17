class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> traverselist = new ArrayList<>();
        mainfunc(root, traverselist);
        return traverselist;
    }

    public void mainfunc(TreeNode root, List<Integer> li){
        if(root != null){
            mainfunc(root.left, li);
            li.add(root.val);
            mainfunc(root.right, li);
        }
    }
}
