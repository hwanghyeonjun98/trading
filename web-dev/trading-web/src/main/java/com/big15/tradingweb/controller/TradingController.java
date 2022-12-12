package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.InvestingDto;
import com.big15.tradingweb.mapper.InvestingMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import javax.websocket.server.PathParam;
import java.util.List;
import java.util.Locale;

@Controller
@RequestMapping("/")
@Slf4j
public class TradingController {

	private InvestingMapper mapper;

	public TradingController(InvestingMapper mapper) {
		this.mapper = mapper;
	}

	// 브라우저 체크
	// 브라우저가 인터넷 익스플로러면 다른 브라우저 접속, 다운로드 안내 페이지로 이동
	@GetMapping("/")
	public String browserCheck(HttpServletRequest request, Locale locale, Model model) {
		String userAgent = request.getHeader("User-Agent");

		if (userAgent.indexOf("Trident") > -1) {
			model.addAttribute("msg", "Internet Explorer는 호환되지 않는 브라우저 입니다.");
			return "/errors/browser_info";
		}

		return "index";
	}

	@GetMapping("/dataview/data")
	public String dataDefultList(Model model) {
		List<InvestingDto> defaultData = mapper.dataDefultList();
		model.addAttribute("dataList", defaultData);
		return "/dataview/data";
	}

	@RequestMapping("/dataview/data/{names}")
	public String dataView(@PathVariable String names, Model model) {
		List<InvestingDto> list_ = mapper.dataList(names);
		model.addAttribute("dataList", list_);
		model.addAttribute("dataName", names);
		return "/dataview/data";
	}

}
