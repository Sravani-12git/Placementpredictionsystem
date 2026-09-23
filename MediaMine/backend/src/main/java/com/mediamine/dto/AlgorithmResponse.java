package com.mediamine.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;
import java.util.Map;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AlgorithmResponse {
    private String algorithm;
    private String text;
    private String pattern;
    private List<Integer> matches;
    private Integer count;
    private long executionTimeNs;
    
    // Algorithm specific outputs
    private int[] lpsArray;
    private int[] zArray;
    private int[] suffixArray;
    private int[] lcpArray;
    private Map<String, List<Integer>> keywordMatches;
    
    // DP outputs
    private Integer distance;
    private Integer cost;
    private int[][] dpMatrix;
    private List<String> suggestions;
    private String longestCommonPhrase;
    private Double similarityScore;
    private List<String> commonPhrases;
    
    // Bitmask / Matrix chain
    private List<String> selectedCategories;
    private Integer bitmaskValue;
    private Integer totalScore;
    private String optimalParenthesization;
    
    private String complexityInfo;
}
