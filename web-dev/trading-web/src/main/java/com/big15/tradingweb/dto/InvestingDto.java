package com.big15.tradingweb.dto;

import lombok.Data;

@Data
public class InvestingDto {
    private String dates;
    private String closes;
    private String opens;
    private String highs;
    private String lows;
    private String volumes;
    private double changes;
}

