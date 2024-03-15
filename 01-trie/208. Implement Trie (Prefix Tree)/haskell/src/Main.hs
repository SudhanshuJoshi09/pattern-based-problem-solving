module Main where

import qualified Data.Map.Strict as M

data Trie = TrieNode String (M.Map Char Trie) | TrieLeaf String deriving (Eq, Show)

buildTrie :: [Char] -> Trie
buildTrie (curr:suffix) =

insert :: [Char] -> Trie -> String -> Trie
insert [] trie _ = trie
insert (curr:suffix) trie prefix =
  case trie of
    TrieNode triePrefix childrenMapping ->
    TrieLeaf leafPrefix ->

main :: IO ()
main = do
  print $ newTrie
  putStrLn "Hello, Haskell!"
  where
    newTrie = TrieLeaf $ T.pack "Something"
