package com.mediamine.service.suffix;

import org.springframework.stereotype.Service;
import java.util.Arrays;

/**
 * Suffix Array Data Structure & Construction
 * 
 * Problem: Compute array of sorted suffix indices of a text T of length n.
 * Idea: Sort all suffixes T[i..n-1] lexicographically.
 * 
 * Algorithm Steps:
 * 1. Store integer suffixes and sort using standard lexicographical comparison.
 * 2. Return array of starting indices of sorted suffixes.
 * 
 * Time Complexity: Construction O(n^2 log n) using standard string comparison / O(n log^2 n) radix doubling.
 * Space Complexity: O(n) for suffix indices.
 */
@Service
public class SuffixArray {

    public static class Suffix implements Comparable<Suffix> {
        public int index;
        public String suffixText;

        public Suffix(int index, String suffixText) {
            this.index = index;
            this.suffixText = suffixText;
        }

        @Override
        public int compareTo(Suffix other) {
            return this.suffixText.compareTo(other.suffixText);
        }
    }

    public int[] buildSuffixArray(String text) {
        if (text == null || text.isEmpty()) {
            return new int[0];
        }
        int n = text.length();
        Suffix[] suffixes = new Suffix[n];

        for (int i = 0; i < n; i++) {
            suffixes[i] = new Suffix(i, text.substring(i));
        }

        Arrays.sort(suffixes);

        int[] sa = new int[n];
        for (int i = 0; i < n; i++) {
            sa[i] = suffixes[i].index;
        }
        return sa;
    }
}
