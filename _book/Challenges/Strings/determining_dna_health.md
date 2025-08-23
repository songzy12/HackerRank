<https://www.hackerrank.com/challenges/determining-dna-health/problem?isFullScreen=false>

TL;DR: The solution here scored 47.7/50, and got TLE on test case 7/8/9.

## Multi String Matching

### KMP

<https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm>

### Trie

<https://en.wikipedia.org/wiki/Trie>

### Aho-Corasick

<https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm>

## Range Sum Query

### Prefix Sum

<https://en.wikipedia.org/wiki/Prefix_sum>

### Fenwick Tree

<https://en.wikipedia.org/wiki/Fenwick_tree>

### Segment Tree

<https://en.wikipedia.org/wiki/Segment_tree>

## Solution: AC + Prefix Sum

## Optimization

```
$ python3 -m cProfile -s time determining_dna_health.py  < tmp/input07.txt
```

```
0 7353994

         30838635 function calls (30838629 primitive calls) in 11.056 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1261351    2.020    0.000    2.849    0.000 determining_dna_health.py:123(_insert_dict_suffix_link)
  1261351    1.745    0.000    1.745    0.000 determining_dna_health.py:25(__init__)
  1261350    1.607    0.000    1.870    0.000 determining_dna_health.py:87(_insert_suffix_link)
        1    1.502    1.502    3.655    3.655 determining_dna_health.py:70(insert_suffix_links)
        1    1.331    1.331    4.371    4.371 determining_dna_health.py:109(insert_dict_suffix_links)
 16074184    1.185    0.000    1.185    0.000 determining_dna_health.py:42(is_head)
   100000    1.085    0.000    2.835    0.000 determining_dna_health.py:58(insert_word)
  2522700    0.152    0.000    0.152    0.000 {method 'add' of 'set' objects}
  2706063    0.085    0.000    0.085    0.000 {built-in method builtins.len}
     1000    0.080    0.000    0.147    0.000 determining_dna_health.py:152(search)
  2522702    0.080    0.000    0.080    0.000 {method 'append' of 'collections.deque' objects}
  2522702    0.076    0.000    0.076    0.000 {method 'popleft' of 'collections.deque' objects}
    99919    0.035    0.000    0.056    0.000 determining_dna_health.py:178(output)
        1    0.029    0.029   10.890   10.890 determining_dna_health.py:47(build_trie)
    99919    0.015    0.000    0.021    0.000 determining_dna_health.py:174(compute_health_sum_interval)
        1    0.008    0.008   11.056   11.056 determining_dna_health.py:14(<module>)
   201000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
     1002    0.006    0.000    0.006    0.000 {method 'split' of 'str' objects}
     1004    0.003    0.000    0.004    0.000 {built-in method builtins.input}
    99919    0.003    0.000    0.003    0.000 {built-in method _bisect.bisect_right}
    99919    0.003    0.000    0.003    0.000 {built-in method _bisect.bisect_left}
      357    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.create_dynamic}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
      357    0.000    0.000    0.001    0.000 codecs.py:319(decode)
     1068    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
      357    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
       10    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        1    0.000    0.000    0.000    0.000 {built-in method io.open_code}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1505(find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:121(_path_join)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:123(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1374(_get_spec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:901(_find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(cache_from_source)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1002(_find_and_load)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:916(get_code)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:486(_init_module_attrs)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:166(_get_module_lock)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       36    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:231(_verbose_message)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:659(_load_unlocked)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:87(acquire)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1036(get_data)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
       34    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1337(_path_importer_cache)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:696(spec_from_file_location)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:135(_path_stat)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:558(module_from_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:127(_path_split)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:112(release)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:79(_unpack_uint32)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:491(_get_cached)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
      3/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1500(_get_spec)
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:560(_classify_pyc)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:645(_compile_bytecode)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:64(_relax_case)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:385(cached)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1171(create_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1406(find_spec)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:878(__exit__)
       13    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:156(__enter__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:351(__init__)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap_external>:844(exec_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:185(cb)
      2/1    0.000    0.000   11.056   11.056 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:129(<genexpr>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:874(__enter__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:175(_path_isabs)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:145(_path_is_mode_type)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:736(find_spec)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:398(parent)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:811(find_spec)
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:593(_validate_timestamp_pyc)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1179(exec_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1033(_handle_fromlist)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:154(_path_isfile)
        2    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:160(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:523(_check_name_wrapper)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1155(__init__)
        3    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:152(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1077(path_stats)
        4    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:18(Node)
        4    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        3    0.000    0.000    0.000    0.000 {built-in method from_bytes}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        4    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        2    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1006(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:406(has_location)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:841(create_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1031(get_filename)
```

### No precomputation of dictionary suffix links

We remove the precomputation of dictionary suffix links, the time cost is reduced from 11.056 seconds to 6.576 seconds:

* `_insert_dict_suffix_link`: 2.020 -> 0
* `insert_dict_suffix_links`: 1.331 -> 0
* `output`: 0.035 -> 0.117

```
0 7353994
         13780609 function calls (13780603 primitive calls) in 6.576 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1261351    1.730    0.000    1.730    0.000 determining_dna_health.py:25(__init__)
  1261350    1.589    0.000    1.846    0.000 determining_dna_health.py:87(_insert_suffix_link)
        1    1.393    1.393    3.517    3.517 determining_dna_health.py:70(insert_suffix_links)
   100000    1.075    0.000    2.810    0.000 determining_dna_health.py:58(insert_word)
  4843259    0.344    0.000    0.344    0.000 determining_dna_health.py:42(is_head)
    99919    0.117    0.000    0.135    0.000 determining_dna_health.py:178(output)
  1261350    0.079    0.000    0.079    0.000 {method 'add' of 'set' objects}
     1000    0.067    0.000    0.211    0.000 determining_dna_health.py:152(search)
  2224120    0.062    0.000    0.062    0.000 {built-in method builtins.len}
  1261351    0.039    0.000    0.039    0.000 {method 'append' of 'collections.deque' objects}
  1261351    0.038    0.000    0.038    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.019    0.019    6.347    6.347 determining_dna_health.py:47(build_trie)
        1    0.008    0.008    6.576    6.576 determining_dna_health.py:14(<module>)
   201000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
     1002    0.006    0.000    0.006    0.000 {method 'split' of 'str' objects}
     1004    0.003    0.000    0.004    0.000 {built-in method builtins.input}
      357    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.create_dynamic}
      357    0.000    0.000    0.000    0.000 codecs.py:319(decode)
     1068    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      357    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
       10    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1505(find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method io.open_code}
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:121(_path_join)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:123(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1374(_get_spec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:901(_find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1002(_find_and_load)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(cache_from_source)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:486(_init_module_attrs)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:659(_load_unlocked)
       36    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:231(_verbose_message)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:166(_get_module_lock)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:916(get_code)
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:174(compute_health_sum_interval)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:87(acquire)
       34    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1036(get_data)
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1337(_path_importer_cache)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:696(spec_from_file_location)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:135(_path_stat)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:112(release)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:558(module_from_spec)
      3/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:79(_unpack_uint32)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:645(_compile_bytecode)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:491(_get_cached)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:127(_path_split)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:560(_classify_pyc)
      2/1    0.000    0.000    6.576    6.576 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:64(_relax_case)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1171(create_module)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:385(cached)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:185(cb)
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1500(_get_spec)
       13    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:844(exec_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1406(find_spec)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:878(__exit__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:156(__enter__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:351(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:874(__enter__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:129(<genexpr>)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:398(parent)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:175(_path_isabs)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:736(find_spec)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:811(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1179(exec_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:145(_path_is_mode_type)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:593(_validate_timestamp_pyc)
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:154(_path_isfile)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:160(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1033(_handle_fromlist)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:523(_check_name_wrapper)
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        3    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1077(path_stats)
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:18(Node)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:152(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1155(__init__)
        4    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1006(__init__)
        4    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {built-in method from_bytes}
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        4    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        2    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_left}
        2    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:406(has_location)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        1    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:841(create_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1031(get_filename)
```

### Lazy init index and prefix sum

This can reduce the time cost from 6.576 seconds to 6.057 seconds

* `__init__`: 1.730 -> 1.037
* `insert_word`: 1.075 -> 1.324

```0 7353994
         13001200 function calls (13001194 primitive calls) in 6.057 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1261350    1.570    0.000    1.829    0.000 determining_dna_health.py:90(_insert_suffix_link)
        1    1.369    1.369    3.478    3.478 determining_dna_health.py:73(insert_suffix_links)
   100000    1.324    0.000    2.367    0.000 determining_dna_health.py:58(insert_word)
  1261351    1.037    0.000    1.037    0.000 determining_dna_health.py:25(__init__)
  4843259    0.351    0.000    0.351    0.000 determining_dna_health.py:42(is_head)
    99919    0.098    0.000    0.098    0.000 determining_dna_health.py:181(output)
  1261350    0.077    0.000    0.077    0.000 {method 'add' of 'set' objects}
     1000    0.067    0.000    0.174    0.000 determining_dna_health.py:155(search)
  1444711    0.043    0.000    0.043    0.000 {built-in method builtins.len}
  1261351    0.039    0.000    0.039    0.000 {method 'append' of 'collections.deque' objects}
  1261351    0.038    0.000    0.038    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.019    0.019    5.864    5.864 determining_dna_health.py:47(build_trie)
        1    0.008    0.008    6.057    6.057 determining_dna_health.py:14(<module>)
   201000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
     1002    0.006    0.000    0.006    0.000 {method 'split' of 'str' objects}
     1004    0.005    0.000    0.005    0.000 {built-in method builtins.input}
      357    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.create_dynamic}
      357    0.000    0.000    0.000    0.000 codecs.py:319(decode)
     1068    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      357    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
       10    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1505(find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method io.open_code}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:121(_path_join)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:123(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1374(_get_spec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:901(_find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(cache_from_source)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1002(_find_and_load)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:486(_init_module_attrs)
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:177(compute_health_sum_interval)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:166(_get_module_lock)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:916(get_code)
       36    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:231(_verbose_message)
      2/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:659(_load_unlocked)
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:87(acquire)
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
       34    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1036(get_data)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1337(_path_importer_cache)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:696(spec_from_file_location)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:135(_path_stat)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:558(module_from_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
      3/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:112(release)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:491(_get_cached)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:127(_path_split)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:645(_compile_bytecode)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:79(_unpack_uint32)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:560(_classify_pyc)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1500(_get_spec)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:385(cached)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:64(_relax_case)
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1171(create_module)
       13    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:844(exec_module)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:878(__exit__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1406(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:156(__enter__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:175(_path_isabs)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:129(<genexpr>)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:351(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:185(cb)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:874(__enter__)
      2/1    0.000    0.000    6.057    6.057 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:811(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:736(find_spec)
       10    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1179(exec_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:145(_path_is_mode_type)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:398(parent)
        3    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:154(_path_isfile)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:160(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1033(_handle_fromlist)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:593(_validate_timestamp_pyc)
        3    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        4    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:152(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:523(_check_name_wrapper)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1077(path_stats)
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:18(Node)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1155(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        2    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        2    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        3    0.000    0.000    0.000    0.000 {built-in method from_bytes}
        2    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1006(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:406(has_location)
        2    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1031(get_filename)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_left}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:841(create_module)
```

### Inline is_head

Time cost reduced from 6.057 seconds to 5.776 seconds

* `is_head`: 0.351 -> 0

```
0 7353994
         8157941 function calls (8157935 primitive calls) in 5.776 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1261350    1.571    0.000    1.571    0.000 determining_dna_health.py:86(_insert_suffix_link)
        1    1.354    1.354    3.128    3.128 determining_dna_health.py:69(insert_suffix_links)
  1261351    1.199    0.000    1.199    0.000 determining_dna_health.py:25(__init__)
   100000    1.195    0.000    2.400    0.000 determining_dna_health.py:54(insert_word)
    99919    0.126    0.000    0.126    0.000 determining_dna_health.py:134(output)
  1261350    0.087    0.000    0.087    0.000 {method 'add' of 'set' objects}
     1000    0.077    0.000    0.208    0.000 determining_dna_health.py:108(search)
  1444711    0.045    0.000    0.045    0.000 {built-in method builtins.len}
  1261351    0.039    0.000    0.039    0.000 {method 'append' of 'collections.deque' objects}
  1261351    0.036    0.000    0.036    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.020    0.020    5.548    5.548 determining_dna_health.py:43(build_trie)
        1    0.009    0.009    5.776    5.776 determining_dna_health.py:14(<module>)
   201000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
     1002    0.006    0.000    0.006    0.000 {method 'split' of 'str' objects}
     1004    0.004    0.000    0.004    0.000 {built-in method builtins.input}
      357    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.create_dynamic}
      357    0.000    0.000    0.001    0.000 codecs.py:319(decode)
     1068    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      357    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
       10    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1505(find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method io.open_code}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:121(_path_join)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:123(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1374(_get_spec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:901(_find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(cache_from_source)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1002(_find_and_load)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:486(_init_module_attrs)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:659(_load_unlocked)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:166(_get_module_lock)
       36    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:231(_verbose_message)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:916(get_code)
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:130(compute_health_sum_interval)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:87(acquire)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1337(_path_importer_cache)
       34    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1036(get_data)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:696(spec_from_file_location)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:135(_path_stat)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:558(module_from_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:112(release)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:79(_unpack_uint32)
      3/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:127(_path_split)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:491(_get_cached)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:645(_compile_bytecode)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:64(_relax_case)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:560(_classify_pyc)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1500(_get_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1171(create_module)
      2/1    0.000    0.000    5.776    5.776 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:385(cached)
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:878(__exit__)
       13    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:185(cb)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:351(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1406(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:156(__enter__)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap_external>:844(exec_module)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:129(<genexpr>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:874(__enter__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:736(find_spec)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:175(_path_isabs)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:398(parent)
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:145(_path_is_mode_type)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:154(_path_isfile)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:811(find_spec)
       10    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1033(_handle_fromlist)
        3    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1179(exec_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:593(_validate_timestamp_pyc)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:160(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:523(_check_name_wrapper)
        4    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        3    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
        2    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:152(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1155(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1077(path_stats)
        2    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:18(Node)
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        4    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1006(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method from_bytes}
        2    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        2    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:406(has_location)
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_left}
        1    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1031(get_filename)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:841(create_module)
```

### BFS no need to record visited node.

Time for test case 7 reduced to 5.183 seconds.

```
0 7353994
         6896591 function calls (6896585 primitive calls) in 5.183 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1261350    1.548    0.000    1.548    0.000 determining_dna_health.py:78(_insert_suffix_link)
   100000    1.167    0.000    2.280    0.000 determining_dna_health.py:49(insert_word)
  1261351    1.107    0.000    1.107    0.000 determining_dna_health.py:25(__init__)
        1    1.059    1.059    2.715    2.715 determining_dna_health.py:63(insert_suffix_links)
    99919    0.094    0.000    0.094    0.000 determining_dna_health.py:126(output)
     1000    0.060    0.000    0.159    0.000 determining_dna_health.py:100(calculate_dna_health)
  1444711    0.043    0.000    0.043    0.000 {built-in method builtins.len}
  1261351    0.035    0.000    0.035    0.000 {method 'append' of 'collections.deque' objects}
  1261351    0.033    0.000    0.033    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.012    0.012    5.006    5.006 determining_dna_health.py:39(build_aho_corasick_automaton)
        1    0.008    0.008    5.183    5.183 determining_dna_health.py:14(<module>)
   201000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
     1002    0.006    0.000    0.006    0.000 {method 'split' of 'str' objects}
     1004    0.003    0.000    0.003    0.000 {built-in method builtins.input}
      357    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.create_dynamic}
      357    0.000    0.000    0.000    0.000 codecs.py:319(decode)
     1068    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      357    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
       10    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1505(find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method io.open_code}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:121(_path_join)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:123(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1374(_get_spec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:901(_find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(cache_from_source)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1002(_find_and_load)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:486(_init_module_attrs)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       36    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:231(_verbose_message)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:166(_get_module_lock)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:659(_load_unlocked)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:916(get_code)
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:122(compute_range_sum)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:87(acquire)
       34    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1036(get_data)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:696(spec_from_file_location)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1337(_path_importer_cache)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:135(_path_stat)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:112(release)
      3/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:558(module_from_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:491(_get_cached)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:127(_path_split)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:645(_compile_bytecode)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:79(_unpack_uint32)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:385(cached)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1500(_get_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:560(_classify_pyc)
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:64(_relax_case)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1171(create_module)
       13    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:185(cb)
      2/1    0.000    0.000    5.183    5.183 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:175(_path_isabs)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap_external>:844(exec_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:156(__enter__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:129(<genexpr>)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1406(find_spec)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:874(__enter__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:878(__exit__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:351(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:736(find_spec)
       10    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
       12    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1179(exec_module)
       10    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:398(parent)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:811(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:593(_validate_timestamp_pyc)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:154(_path_isfile)
        3    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:160(__exit__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:145(_path_is_mode_type)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1033(_handle_fromlist)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1155(__init__)
        4    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        3    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:152(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:523(_check_name_wrapper)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1077(path_stats)
        2    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        2    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {built-in method from_bytes}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:18(Node)
        4    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1006(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        4    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:406(has_location)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1031(get_filename)
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_left}
        1    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
        2    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:841(create_module)
```

### Optimize how to build the suffix links

This reduced the time cost of test case 7 to 4.264 seconds.

```
0 7353994
         5635238 function calls (5635232 primitive calls) in 4.264 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.702    1.702    1.800    1.800 determining_dna_health.py:62(insert_suffix_links)
   100000    1.188    0.000    2.275    0.000 determining_dna_health.py:48(insert_word)
  1261351    1.080    0.000    1.080    0.000 determining_dna_health.py:25(__init__)
    99919    0.092    0.000    0.092    0.000 determining_dna_health.py:108(output)
     1000    0.061    0.000    0.157    0.000 determining_dna_health.py:80(calculate_dna_health)
  1261351    0.035    0.000    0.035    0.000 {method 'items' of 'dict' objects}
  1261350    0.032    0.000    0.032    0.000 {method 'append' of 'collections.deque' objects}
  1261350    0.031    0.000    0.031    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.012    0.012    4.087    4.087 determining_dna_health.py:40(build_aho_corasick_automaton)
        1    0.008    0.008    4.264    4.264 determining_dna_health.py:14(<module>)
     1002    0.006    0.000    0.006    0.000 {method 'split' of 'str' objects}
   201000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
   183359    0.004    0.000    0.004    0.000 {built-in method builtins.len}
     1004    0.004    0.000    0.004    0.000 {built-in method builtins.input}
      357    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.create_dynamic}
      357    0.000    0.000    0.001    0.000 codecs.py:319(decode)
     1068    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
      357    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
       10    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1505(find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method io.open_code}
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:121(_path_join)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:123(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1374(_get_spec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:901(_find_spec)
        1    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(cache_from_source)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1002(_find_and_load)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:486(_init_module_attrs)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:166(_get_module_lock)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:916(get_code)
       36    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:231(_verbose_message)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:659(_load_unlocked)
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:102(compute_range_sum)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:87(acquire)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
       34    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1036(get_data)
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:696(spec_from_file_location)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1337(_path_importer_cache)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:135(_path_stat)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:112(release)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:558(module_from_spec)
      3/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:127(_path_split)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:491(_get_cached)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:645(_compile_bytecode)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:64(_relax_case)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:560(_classify_pyc)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:79(_unpack_uint32)
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1171(create_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1500(_get_spec)
       13    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:385(cached)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:878(__exit__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1406(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:156(__enter__)
      2/1    0.000    0.000    4.264    4.264 {built-in method builtins.exec}
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap_external>:844(exec_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:185(cb)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:129(<genexpr>)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:175(_path_isabs)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:874(__enter__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:351(__init__)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:736(find_spec)
       10    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:811(find_spec)
       10    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1179(exec_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:145(_path_is_mode_type)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:398(parent)
        3    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:160(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1033(_handle_fromlist)
        3    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:154(_path_isfile)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:152(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:523(_check_name_wrapper)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:593(_validate_timestamp_pyc)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        4    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1155(__init__)
        2    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1077(path_stats)
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        3    0.000    0.000    0.000    0.000 {built-in method from_bytes}
        4    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 determining_dna_health.py:18(Node)
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        2    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        2    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1006(__init__)
        2    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:406(has_location)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1031(get_filename)
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_left}
        1    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:841(create_module)
```

## Reference

1. AC + Fenwick Tree: https://www.hackerrank.com/challenges/determining-dna-health/editorial
2. Hash + Prefix Sum: https://www.hackerrank.com/challenges/determining-dna-health/forum/comments/545570
3. AC + Persistent Segment Tree: https://www.hackerrank.com/challenges/determining-dna-health/forum/comments/532519
4. Compressed trie + Segment tree: https://www.hackerrank.com/challenges/determining-dna-health/forum/comments/1325327
5. https://www.hackerrank.com/challenges/determining-dna-health/leaderboard?filter=python3&filter_on=language&page=1
