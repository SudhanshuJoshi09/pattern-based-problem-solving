{-# LANGUAGE TemplateHaskell #-}
module Main where

import qualified Data.Map.Strict as M

data Trie = Trie
  { path :: String
  , links :: M.Map Char Trie
  } deriving (Eq, Show)

buildTrie :: [Char] -> [Char] -> Trie
buildTrie [curr] prefix =
  Trie
  { path = prefix ++ [curr]
  , links = M.empty
  }
buildTrie [] prefix = 
  Trie
  { path = prefix
  , links = M.empty
  }
buildTrie (curr:suffix) prefix =
  let suffixTrie = buildTrie suffix $ prefix ++ [curr]
  in Trie
  { path = prefix ++ [curr]
  , links = M.insert curr suffixTrie M.empty
  }

insert :: [Char] -> Trie -> [Char] -> Trie
insert [] trie _ = trie
insert (curr:suffix) trie prefix =
  case (M.lookup curr links) of
    Just nextTrieVal -> insert suffix nextTrieVal $ prefix ++ [curr]
    Nothing ->
      let buildTrieVal = buildTrie (curr:suffix) (currPath)
          updatedLinks = M.insert curr buildTrieVal links
      in trie {
        links = updatedLinks
      }
  where
    links = getLinks trie
    currPath = getPath trie
  
getLinks :: Trie -> M.Map Char Trie
getLinks = links

getPath :: Trie -> String
getPath = path

main :: IO ()
main = do
  print $ newTrie2
  where
    newTrie =
      Trie
        { path = ""
        , links = M.empty
        }

    newTrie1 = insert "Hello, World" newTrie ""
    newTrie2 = insert "Hello, Haskell" newTrie ""
