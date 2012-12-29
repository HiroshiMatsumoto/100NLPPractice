#! /usr/bin/env python
#-*- coding: utf-8 -*-

exam = dict()

exam["dave"] = dict(math=76,science=92)
exam["smith"] = dict(math=78,science=100)
exam["smith"] = dict(math=7,science=10)
exam["dave"].update(social_study=7,art=9)

print exam
