#!/bin/bash


cat README.md |
	grep -v '^## Content ##$' | grep '^###*' -B 1 | grep -v '^--$'  |
	while read REF ; read H
	 do
	    H="$(echo $H | sed 's/^\(#*\)## /\1- [/' | sed 's/#/ /g' | sed 's/ *$//')"
	    REF="$(echo $REF | sed 's/^.*name="\([^"]*\)".*$/\1/')"
	    : ${REF:=-------------- NOT SET --------------}
		echo "$H](#$REF)"
	done