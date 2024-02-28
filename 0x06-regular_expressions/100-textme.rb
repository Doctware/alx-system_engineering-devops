#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|to:|flags:)[a-zA-Z0-9+-:][^\]]{1,}/).join(',')
