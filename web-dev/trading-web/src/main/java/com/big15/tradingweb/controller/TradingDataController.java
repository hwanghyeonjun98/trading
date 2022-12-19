package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.InvestingDto;
import com.big15.tradingweb.mapper.InvestingMapper;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@Slf4j
@Controller
@AllArgsConstructor
@RequestMapping("/dataview")
public class TradingDataController {
	private InvestingMapper mapper;

	@GetMapping("/data")
	public String dataDefultList(Model model) {
		List<InvestingDto> defaultData = mapper.dataDefultList();
		model.addAttribute("dataList", defaultData);
		return "/dataview/data";
	}

	@RequestMapping("/data/{names}")
	public String dataView(@PathVariable String names, Model model) {
		List<InvestingDto> list_ = mapper.dataList(names);
		model.addAttribute("dataList", list_);
		model.addAttribute("dataName", names);
		return "/dataview/data";
	}
}
