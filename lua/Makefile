NAME := yamlstar
VERSION := 0.0.1
ROCKSPEC := $(NAME)-$(VERSION)-1.rockspec

publish:
	: git tag lua-$(VERSION)
	: git push
	: git push --tags
	./luarocks make
	./luarocks build
	./luarocks pack $(ROCKSPEC)
	./luarocks upload \
	    $(ROCKSPEC) \
	    --api-key $(LUAROCKS_API_KEY)

clean:
	$(RM) -r ./$(NAME)/
	$(RM) *.rock
