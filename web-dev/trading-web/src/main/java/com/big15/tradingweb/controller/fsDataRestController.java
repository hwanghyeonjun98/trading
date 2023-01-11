package com.big15.tradingweb.controller;


import com.big15.tradingweb.dto.FsDto;
import com.big15.tradingweb.dto.FsListDto;
import com.big15.tradingweb.mapper.fsData.fsDataMapper;
import com.big15.tradingweb.mapper.webData.FsDataListMapper;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Slf4j
@RestController
@AllArgsConstructor
@RequestMapping("/api/data")
public class fsDataRestController {

	private fsDataMapper fsDataMapper;
	private FsDataListMapper fsDataListMapper;

	@RequestMapping("/fsInfo/{search}")
	public List<FsDto> fsList(@PathVariable("search") String fsData) {
		return fsDataMapper.fsInfoList(fsData);
	}

	@RequestMapping("/fsList")
	public List<FsListDto> stockList() {
		return fsDataListMapper.stockList();
	}

}
