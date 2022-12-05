package com.big15.tradingweb.dto;

import lombok.Data;

@Data
public class InvestingDto {
    private String dates;
    private double closes;
    private double opens;
    private double highs;
    private double lows;
    private double volumes;
    private double changes;
}

