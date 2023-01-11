package com.big15.tradingweb.config;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.SqlSessionTemplate;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

import javax.sql.DataSource;

@Configuration
@MapperScan(value = "com.big15.tradingweb.mapper.fsData", sqlSessionFactoryRef = "factory2")
public class FaDataConfig {

	@Bean(name = "fsdata")
	@ConfigurationProperties(prefix = "spring.datasource.fsdata")
	public DataSource doSource() {
		return DataSourceBuilder.create().build();
	}

	@Bean(name = "factory2")
	public SqlSessionFactory sqlSesstionFactory(@Qualifier("fsdata") DataSource dataSource) throws Exception {
		SqlSessionFactoryBean sqlSessionFactory = new SqlSessionFactoryBean();
		sqlSessionFactory.setDataSource(dataSource);
		sqlSessionFactory.setTypeAliasesPackage("com.big15.tradingweb.mapper.fsData");
		sqlSessionFactory.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:/mybatis/mapper/fsData/*.xml"));
		return sqlSessionFactory.getObject();
	}

	@Bean(name = "sqlSession2")
	public SqlSessionTemplate sqlSession(SqlSessionFactory sqlSessionFactory) {
		return new SqlSessionTemplate(sqlSessionFactory);
	}
}
