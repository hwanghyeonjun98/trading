package com.big15.tradingweb.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.RequestDispatcher;
import javax.servlet.http.HttpServletRequest;

// 에러 처리 컨트롤러
@Slf4j
@Controller
public class Error implements ErrorController {
	private String ERROR_TEMPLATES_PATH = "/errors/";

	@RequestMapping(value = "*")
	public String handleError(HttpServletRequest request) {
		Object status = request.getAttribute(RequestDispatcher.ERROR_STATUS_CODE);
		if (status != null) {
			log.error("error code : " + status.toString());
			int statusCode = Integer.parseInt(status.toString());
			if (statusCode == HttpStatus.NOT_FOUND.value()) {
				return ERROR_TEMPLATES_PATH + "404";
			}

			if (statusCode == HttpStatus.FORBIDDEN.value()) {
				return ERROR_TEMPLATES_PATH + "403";
			}

			if (statusCode == HttpStatus.INTERNAL_SERVER_ERROR.value()) {
				return ERROR_TEMPLATES_PATH + "500";
			}
		}
		return "index";
	}
}
