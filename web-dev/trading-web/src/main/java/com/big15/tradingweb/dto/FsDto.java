package com.big15.tradingweb.dto;

import lombok.Data;

@Data
public class FsDto {
	private String _date;
	private String 재무제표_재무상태표_유동자산;
	private String 재무제표_재무상태표_비유동자산;
	private String 재무제표_재무상태표_자산총계;
	private String 재무제표_재무상태표_유동부채;
	private String 재무제표_재무상태표_비유동부채;
	private String 재무제표_재무상태표_부채총계;
	private String 재무제표_재무상태표_자본금;
	private String 재무제표_재무상태표_이익잉여금;
	private String 재무제표_재무상태표_자본총계;

	private String 재무제표_손익계산서_매출액;
	private String 재무제표_손익계산서_영업이익;
	private String 재무제표_손익계산서_법인세차감전_순이익;
	private String 재무제표_손익계산서_당기순이익;
	private String 연결재무제표_재무상태표_유동자산;
	private String 연결재무제표_재무상태표_비유동자산;
	private String 연결재무제표_재무상태표_자산총계;
	private String 연결재무제표_재무상태표_유동부채;
	private String 연결재무제표_재무상태표_비유동부채;
	private String 연결재무제표_재무상태표_부채총계;

	private String 연결재무제표_재무상태표_자본금;
	private String 연결재무제표_재무상태표_이익잉여금;

	private String 연결재무제표_재무상태표_자본총계;
	private String 연결재무제표_손익계산서_매출액;
	private String 연결재무제표_손익계산서_영업이익;
	private String 연결재무제표_손익계산서_법인세차감전_순이익;
	private String 연결재무제표_손익계산서_당기순이익;

}
