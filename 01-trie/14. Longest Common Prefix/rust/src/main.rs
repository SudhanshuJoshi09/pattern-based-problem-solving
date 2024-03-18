struct Solution {
    strs: Vec<String>,
}

impl Solution {
    pub fn new(strs: Vec<String>) -> Self {
        Self { strs }
    }

    pub fn longest_common_prefix(self) -> String {
        let strs = self.strs;
        if strs.is_empty() {
            return String::new();
        }

        for (i, &ch) in strs[0].as_bytes().iter().enumerate() {
            for s in strs.iter().skip(1) {
                if i >= s.len() || s.as_bytes()[i] != ch {
                    return String::from_utf8(strs[0].as_bytes()[..i].to_vec()).unwrap();
                }
            }
        }

        strs[0].clone()
    }
}

fn main() {
    let strs: Vec<String> = ["key1", "key2", "key3", "ke"]
        .iter()
        .map(|&str| str.to_string())
        .collect();
    let solution = Solution::new(strs);
    println!("Result :: {}", solution.longest_common_prefix())
}
