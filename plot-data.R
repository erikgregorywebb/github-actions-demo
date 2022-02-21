# import libraries
library(tidyverse)
library(rvest)
library(scales)

# get links to data files
url = 'https://github.com/erikgregorywebb/github-actions-demo/tree/main/data'
page = read_html(url)
all_paths = page %>% html_nodes('a') %>% html_attr('href')
paths = all_paths[str_detect(all_paths, '/erikgregorywebb/github-actions-demo/blob/main/data/fm-rates')]
links = paste('https://raw.githubusercontent.com/erikgregorywebb/github-actions-demo/main/data/', basename(paths), sep = '')

# loop over, import
datalist = list()
for (i in 1:length(links)) {
  Sys.sleep(.5)
  print(links[i])
  datalist[[i]] = read_csv(links[i]) %>%
    mutate(filename = basename(links[i]))
}
raw = do.call(rbind, datalist)
glimpse(raw)
tail(raw)

# clean
rates = raw %>%
  mutate(rate = as.numeric(str_remove(rate, '%'))) %>%
  mutate(fees = parse_number(fees))

# prepare to plot 
min_date = format(min(rates$datetime), '%B %d, %Y')
max_date = format(max(rates$datetime), '%B %d, %Y')
subtitle_string = paste(min_date, ' to ', max_date, sep = '')

# plot
plot = ggplot(rates, aes(x = datetime, y = rate, col = name)) + 
  geom_line(size = 1.5) + 
  labs(x = '', y = 'Rate (%)', title = 'Average Mortgage Rates', subtitle = subtitle_string, 
       caption = 'Source: Daily scrape of rates posted on freddiemac.com homepage') +
  theme(legend.position = 'top') + 
  theme(legend.title=element_blank()) +
  theme(text = element_text(size = 14))
plot

# export
plot_title = paste('rates-plot-', Sys.Date(), '.png', sep = '')
png(plot_title, width = 9, height = 6, units = 'in', res = 400)
plot
dev.off()
