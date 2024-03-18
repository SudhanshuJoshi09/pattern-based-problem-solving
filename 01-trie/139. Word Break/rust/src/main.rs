use std::collections::HashMap;

#[derive(Debug)]
struct TrieNode {
    children: HashMap<char, TrieNode>,
    is_eow: bool,
}

#[derive(Debug)]
struct Trie {
    trie: TrieNode,
    memo: HashMap<(char, TrieNode), bool>,
}

impl TrieNode {
    pub fn new() -> Self {
        Self {
            children: HashMap::new(),
            is_eow: false,
        }
    }
}

impl Trie {
    pub fn new() -> Self {
        Self {
            trie: TrieNode::new(),
            memo: HashMap::new(),
        }
    }

    fn insert_impl(node: &mut TrieNode, key: &str, idx: usize) {
        if idx == key.len() {
            node.is_eow = true;
            return;
        }

        let curr_key = key.chars().nth(idx).unwrap();
        let tmp_node = TrieNode::new();

        let child = node.children.entry(curr_key).or_insert_with(|| tmp_node);
        Self::insert_impl(child, key, idx + 1);
    }

    pub fn insert(&mut self, key: String) {
        Trie::insert_impl(&mut self.trie, &key, 0);
    }
}

fn main() {
    let mut trie = Trie::new();
    trie.insert("Hello".to_string());
    println!("This is the trie *1: {:?}", trie);
    trie.insert("World".to_string());
    println!("This is the trie *2: {:?}", trie);
}
