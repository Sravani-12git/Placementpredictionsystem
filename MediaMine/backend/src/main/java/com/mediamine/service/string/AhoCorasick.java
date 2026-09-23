package com.mediamine.service.string;

import org.springframework.stereotype.Service;
import java.util.*;

/**
 * Aho-Corasick Multi-Pattern Matching Automaton
 * 
 * Problem: Simultaneously locate all occurrences of a set of pattern keywords P = {p1, p2, ..., pk} in text T.
 * Idea: Combine a Trie of patterns with failure links (similar to KMP prefix function) and output links 
 *       to process text in a single pass.
 * 
 * Algorithm Steps:
 * 1. Build a Trie from all keywords.
 * 2. Compute BFS failure links for all Trie nodes. If a child node has no matching transition, 
 *    follow the failure link of its parent.
 * 3. Construct output links to collect all patterns matched at a particular state.
 * 4. Traverse text T character by character through automaton state transitions.
 * 
 * Time Complexity: Construction O(sum(|pi|)), Search O(|T| + matches)
 * Space Complexity: O(sum(|pi|) * alphabet_size)
 */
@Service
public class AhoCorasick {

    public static class Node {
        public Map<Character, Node> children = new HashMap<>();
        public Node fail;
        public List<String> outputs = new ArrayList<>();
    }

    public Map<String, List<Integer>> search(String text, List<String> keywords) {
        Map<String, List<Integer>> result = new LinkedHashMap<>();
        if (text == null || keywords == null || keywords.isEmpty()) {
            return result;
        }

        for (String kw : keywords) {
            if (kw != null && !kw.isEmpty()) {
                result.put(kw, new ArrayList<>());
            }
        }

        // 1. Build Trie
        Node root = new Node();
        for (String kw : keywords) {
            if (kw == null || kw.isEmpty()) continue;
            Node curr = root;
            for (char ch : kw.toCharArray()) {
                curr = curr.children.computeIfAbsent(ch, k -> new Node());
            }
            curr.outputs.add(kw);
        }

        // 2. Build Failure Links using BFS
        Queue<Node> queue = new LinkedList<>();
        for (Node child : root.children.values()) {
            child.fail = root;
            queue.add(child);
        }

        while (!queue.isEmpty()) {
            Node curr = queue.poll();

            for (Map.Entry<Character, Node> entry : curr.children.entrySet()) {
                char ch = entry.getKey();
                Node child = entry.getValue();

                Node failNode = curr.fail;
                while (failNode != null && !failNode.children.containsKey(ch)) {
                    failNode = failNode.fail;
                }

                if (failNode != null) {
                    child.fail = failNode.children.get(ch);
                    child.outputs.addAll(child.fail.outputs);
                } else {
                    child.fail = root;
                }

                queue.add(child);
            }
        }

        // 3. Process Text
        Node curr = root;
        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);

            while (curr != null && !curr.children.containsKey(ch)) {
                curr = curr.fail;
            }

            if (curr == null) {
                curr = root;
                continue;
            }

            curr = curr.children.get(ch);

            for (String matchedPattern : curr.outputs) {
                int startPos = i - matchedPattern.length() + 1;
                result.get(matchedPattern).add(startPos);
            }
        }

        return result;
    }
}
