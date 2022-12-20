package com.big15.tradingweb.dto;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Data
@Getter
@Setter
public class NewsDto {
    private String newsName;
    private String newsLink;
    private String news;
}
