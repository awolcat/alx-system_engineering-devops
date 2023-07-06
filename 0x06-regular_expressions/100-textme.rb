#!/usr/bin/env ruby
params = ARGV[0].scan(/from:\+?\w+|to:\+?\w+|flags:[10:-]+/).join
puts params.scan(/[^(from|to|flags)]/).join
