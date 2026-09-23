package com.mediamine.repository;

import com.mediamine.entity.SearchQuery;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface SearchQueryRepository extends JpaRepository<SearchQuery, Long> {
    List<SearchQuery> findTop10ByOrderBySearchedAtDesc();
}
