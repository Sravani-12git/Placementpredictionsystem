package com.mediamine.repository;

import com.mediamine.entity.Media;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MediaRepository extends JpaRepository<Media, Long> {

    List<Media> findByMediaType(String mediaType);

    @Query("SELECT m FROM Media m JOIN m.categories c WHERE c.id = :categoryId")
    List<Media> findByCategoryId(@Param("categoryId") Long categoryId);

    @Query("SELECT m FROM Media m WHERE LOWER(m.title) LIKE LOWER(CONCAT('%', :query, '%')) OR LOWER(m.content) LIKE LOWER(CONCAT('%', :query, '%')) OR LOWER(m.transcript) LIKE LOWER(CONCAT('%', :query, '%'))")
    List<Media> searchByKeyword(@Param("query") String query);
}
