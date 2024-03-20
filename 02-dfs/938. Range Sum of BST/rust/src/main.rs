use std::rc::Rc;
use std::cell::RefCell;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

struct Solution {
}

impl Solution {
    pub fn range_sum_bst_impl(root: Option<&Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        if let Some(root) = root {
            let res_root = root.borrow();
            let mut result: i32 = 0;

            if res_root.val >= low && res_root.val <= high {
                result += res_root.val;
            }

            result += Solution::range_sum_bst_impl(res_root.left.as_ref(), low, high);
            result += Solution::range_sum_bst_impl(res_root.right.as_ref(), low, high);

            return result;
        } else {
            return 0;
        }
    }

    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        return Solution::range_sum_bst_impl(root.as_ref(), low, high);
    }

}

fn main() {
    println!("Need to add some basic tests here !");
}
