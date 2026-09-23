package com.mediamine.service.string;

import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;

/**
 * Knuth-Morris-Pratt (KMP) Pattern Matching Algorithm
 * 
 * Problem: Find all starting indices of pattern P of length m in text T of length n.
 * Idea: Avoid re-checking characters that have already been matched by maintaining a 
 *       Longest Prefix-Suffix (LPS) array pi[i], which stores the length of the longest 
 *       proper prefix of P[0..i] that is also a suffix of P[0..i].
 * 
 * Algorithm Steps:
 * 1. Build the LPS table for pattern P.
 * 2. Scan text T with pointer i and pattern P with pointer j.
 * 3. On match (T[i] == P[j]), increment both i and j.
 * 4. If j == m, record match index (i - m) and update j = lps[j - 1].
 * 5. On mismatch (T[i] != P[j]), if j > 0 update j = lps[j - 1] without incrementing i.
 *    If j == 0, increment i.
 * 
 * Time Complexity: O(n + m)
 * Space Complexity: O(m) for the LPS table.
 */
@Service
public class KMP {

    public int[] computeLPSArray(String pattern) {
        if (pattern == null || pattern.isEmpty()) {
            return new int[0];
        }
        int m = pattern.length();
        int[] lps = new int[m];
        int len = 0;
        int i = 1;
        lps[0] = 0;

        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    public List<Integer> search(String text, String pattern) {
        List<Integer> matches = new ArrayList<>();
        if (text == null || pattern == null || pattern.isEmpty() || text.length() < pattern.length()) {
            return matches;
        }

        int n = text.length();
        int m = pattern.length();
        int[] lps = computeLPSArray(pattern);

        int i = 0; // index for text
        int j = 0; // index for pattern

        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }

            if (j == m) {
                matches.add(i - j);
                j = lps[j - 1];
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return matches;
    }
}
