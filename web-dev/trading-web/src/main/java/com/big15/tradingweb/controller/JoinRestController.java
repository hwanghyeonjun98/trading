package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.UserInfoDto;
import com.big15.tradingweb.mapper.JoinMapper;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletResponse;
import javax.websocket.server.PathParam;
import java.io.IOException;
import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("/join")
public class JoinRestController {

	JoinMapper joinMapper;


	@PutMapping("/join")
	public void join(@PathParam("user_id") String user_id, @PathParam("user_pw") String user_pw, @PathParam("user_name") String user_name, @PathParam("user_account") String user_account, HttpServletResponse response) throws IOException {
		int join = joinMapper.join(user_id, user_pw, user_name, user_account);

		if (join == 0) {
			response.getWriter().print("joinFalse");
		}

		if (join == 1) {
			response.getWriter().print("joinTrue");
		}
	}

	@RequestMapping("/idCheck/{user_id}")
	public void idCheck(@PathVariable("user_id") String user_id, HttpServletResponse response) throws IOException {
		List<UserInfoDto> user = joinMapper.idCheck(user_id);

		if (user == null) {
			response.getWriter().print("notId");
		}

		if (user != null) {
			response.getWriter().print("hadId");
		}
	}
}
