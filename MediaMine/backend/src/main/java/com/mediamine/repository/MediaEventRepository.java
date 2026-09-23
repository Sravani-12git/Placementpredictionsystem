package com.mediamine.repository;

import com.mediamine.entity.MediaEvent;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MediaEventRepository extends JpaRepository<MediaEvent, Long> {
    List<MediaEvent> findTop10ByOrderByEventTimeDesc();
    long countByEventType(String eventType);
}
