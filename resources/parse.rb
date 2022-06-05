# Trivial odp2md aiming at extracting links from slides
# s = '<text:a xlink:href="https://expressjs.com/en/resources/template-engines.html" xlink:type="simple">soem tex</text:a>'
# t = '      <draw:page draw:name="Juicy targets: Electron apps" draw:style-name="dp1" draw:master-page-name="OBJECT" presentation:presentation-page-layout-name="AL1T11">'


def get_title(line)
    quotes = line.split('"')
    quotes[1]
end

def fmt_link(line)
    quotes = line.split('"')

    link = quotes[1]
    val = line.split('">')[1]
    text = val.split("</text")[0]

    "[#{text}](#{link})"
end


if __FILE__ == $0

  if ARGV.length != 1 then
      $stderr.puts "Usage: #{$0} file.odp"
      exit 1
  end
  
  file = ARGV[0]
  
  `rm -f content.xml`
  `unzip "#{file}" content.xml`
  raise if $? != 0
  
  `rm -f interesting.txt`
  `xmllint --format content.xml | grep -E "(text:a|draw:page )" > interesting.txt`
  raise if $? != 0
  
  first = true
  title = nil
  f = File.open("interesting.txt")
  f.each_line do |line| 
  
      case line
      when /draw:page /
          title = get_title(line)
          first = true
      when /text:a/
          if first then
              puts "## #{title}"
              first = false
          end
          puts " - #{fmt_link(line)}"
      end
  end

end
