package com.big15.tradingweb.dto;

import lombok.Data;

@Data
public class InvestingDto {
    private String date;
    private double close;
    private double open;
    private double high;
    private double low;
    private double volume;
    private double change;
}

